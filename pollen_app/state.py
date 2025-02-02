import reflex as rx
import json
import os
import requests as req
import json
from datetime import datetime
import dataclasses
from datetime import datetime


class FormState(rx.State):
    data:dict
    provinces:list[str] = ["Almería","Cádiz","Córdoba","Granada","Huelva","Jaén","Málaga","Sevilla"]
    towns_list:list[str] = []
    selected_province:str = ""
    selected_town: str = ""
    pollen_data:dict[str,list] = {}
    dates:list[str]=[]
    
    async def readFile(self):
        file_path = os.path.join(os.path.dirname(__file__),'andalucia.json')
        print("Reading file: "+file_path)

        try:
            with open(file_path,"r") as file:
                self.data = json.load(file)
        except Exception as err:
            print("Error: ",err)
    async def on_load(self):
        print("onload event is trigered")
        await self.readFile()  
    async def _getPollenData(self,lat,long):
        try:
            params={
                "key": os.environ["TOKEN"],
                "location.longitude": str(long),
                "location.latitude": str(lat),
                "days": str(5),
                "languageCode": "ES"
            }
            result = req.get("https://pollen.googleapis.com/v1/forecast:lookup",params=params)
            if result.status_code>=200 and result.status_code <= 299:
                pollen_dict = json.loads(result.text)
                return pollen_dict
            else:
                print("Error obteniendo los datos ", result.status_code )  
                return {}  
        except Exception as e:
            print(e)    
    def on_change_province(self,value:str):
        self.selected_province = value
        towns = self.data[self.selected_province]
        self.towns_list = [town['poblacion'] for town in towns]
        self.selected_town=self.towns_list[0]
    def on_change_town(self,value:str):
        self.selected_town = value
   #     @rx.event    
    async def submit_form(self,form_data:dict):
        index = self.towns_list.index(self.selected_town)
        latitud = self.data[self.selected_province][index]['latitud']
        longitud = self.data[self.selected_province][index]['longitud']
        results =  await self._getPollenData(lat = latitud,long=longitud)
        self.pollen_data={}
        
        for day_reuslt in results["dailyInfo"]:
            reference_date = datetime(day_reuslt["date"]["year"],day_reuslt["date"]["month"],day_reuslt["date"]["day"]).strftime("%d-%m-%Y")
            self.dates.append(reference_date)
     
            for plant in day_reuslt["plantInfo"]:
                plant_name = plant["displayName"]
                indexInfo = plant.get("indexInfo",None)    
                if indexInfo:
                    category = indexInfo.get("value",0)
                else:
                    category = 0   
                if plant_name not in  self.pollen_data:
                    self.pollen_data[plant_name]= [category]
                else:
                    self.pollen_data[plant_name].append(category)  
        print(self.pollen_data)            

