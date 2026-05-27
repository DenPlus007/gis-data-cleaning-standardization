import arcpy

arcpy.env.overwriteOutput = True

input_fc = r"C:\GIS\input.gdb\features"
output_fc = r"C:\GIS\output.gdb\features_clean"

arcpy.management.RepairGeometry(input_fc)

arcpy.management.DeleteIdentical(
    input_fc,
    ["Shape"]
)

arcpy.management.Project(
    input_fc,
    output_fc,
    arcpy.SpatialReference(4326)
)

print("GIS Data Cleaning Process Completed")
