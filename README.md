(Work-In-Progress) 
A full-stack web application built using Django REST Framework and React frontend that models Stardew Valley crops and seasons to help players calculate the most profitable crops for each in-game season.

Status of Project:
- Core features of models (Crops, Seasons, Fertilizer, Fertilizer Quality), serializers, and views implemented
- Custom management commands added for populating crop/season/fertilizer data
- Basic set-up of utility function for crop quality calculations

To-Do:
- Create endpoint for most optimal crops with database aggregation via queryset annotations
- POST endpoint that depends on user models (planning for crop plan/farm save creation)
- Implement React frontend for better interactivity and usability of API
