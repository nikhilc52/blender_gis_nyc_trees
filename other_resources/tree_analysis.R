library(tidyverse)

#read in csv of the tree census
df <- read_csv("2015_Street_Tree_Census_-_Tree_Data_20240718.csv")

#parse data and summarize to find given variables
data <- df |> 
  filter(borough%in%c("Manhattan","Bronx")) |> 
  group_by(nta_name) |> 
  summarize(count=n(),
            countAlive = sum(status=="Alive"),
            countDead = sum(status=="Dead"),
            percentDead = countDead/count)
