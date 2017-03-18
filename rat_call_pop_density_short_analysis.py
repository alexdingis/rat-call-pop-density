##
## this script was not written as a continuous script, it was written in several parts which are broken up
## the intent was to explore the data and perform some geoprocessing operations
## this section was to check the % area that was land, most
##
##
##
##import arcpy, numpy, time
##
workspace                 = "C:\link\to\my\scratch.gdb"
arcpy.env.workspace       = workspace
arcpy.env.overwriteOutput = True
##
##
##
featureClass = "Tracts_RubOut2016_Spatial_Join"
fields       = ["ALAND","AWATER"]
pctList      = []
with arcpy.da.SearchCursor(featureClass, fields) as cursor:
	for row in cursor:
		totalArea = row[0] + row[1]
		pctArea   = row[0] / totalArea
		#print "{0}".format(pctArea)
		pctList.append(pctArea)
maxPCT       = max(pctList)
minPCT       = min(pctList)
print "Max: {0}".format(maxPCT)
print "Min: {0}".format(minPCT)
print "done"
##
## this next section is to add new fields to the attribute table
##
featureClass = "Analysis_Clipped"
newFields    = ["RatCallsCount","Population","PopulationDensity","abvRat","abvPop","abvPopD", "LISA_I", "LISA_CL","LISA_SIG"]
for newField in newFields:
	arcpy.AddField_management(featureClass,newField,"DOUBLE")
##
## the following section is to get the population and population density
##


##
##
##