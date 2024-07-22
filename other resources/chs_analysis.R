library(sf)
library(dplyr)

shape <- as.data.frame(read_sf("CHS_2009_DOHMH_2010B.shp"))

df <- shape |> 
  filter(FIRST_BORO %in% c("Bronx","Man")) |> 
  select(FIRST_BORO, FIRST_UHF_, exercs2)
