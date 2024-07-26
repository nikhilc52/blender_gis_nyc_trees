library(dplyr)
library(gt)

#data from https://en.wikipedia.org/wiki/Race_and_ethnicity_in_New_York_City

df <- data.frame(race=c('White', 'Black', 'Asian', 'Other','Mixed'),
                 racial_compostion=c(.299,.356,.030,.257,.058))

#generate a table of the above values
table <- df |> 
  arrange(-racial_compostion) |> 
  gt() |> 
  opt_align_table_header('center') |> 
  opt_table_font(font=list(google_font(name="Helvetica"))) |> 
  cols_label(racial_compostion="Racial Composition",race="Race") |> 
  cols_align("center") |> 
  tab_header(title="Racial Composition in the Bronx", subtitle="2000 Census") |> 
  tab_style(style=cell_text(size="bigger",weight="bold",transform="uppercase"),
            location = cells_title(groups="title")) |> 
  tab_style(style=cell_fill(color="lightyellow"),
            location = cells_body(rows= race=="Black")) |> 
  fmt_percent(
    columns = racial_compostion,
    decimals=1
  )

#print the table to the viewer
print(table)

#save the table to a path
gtsave(table,"demographics.png",path="/Users/nc7172/Documents/GitHub/blender_gis_nyc_trees/video files")  
