hostname = 'autofocus.paloaltonetworks.com'
# elasticSearch bulk load url and port
elastic_url_port = 'localhost:9200'
# querytype is autofocus for exported queries or hash when reading from hash list
querytype = 'autofocus'
# used for hash inputs; leave as default even if not using
inputfile = 'hash_list.txt'
# type of hash used in the input list when querytype is hash
hashtype = 'sha256'
# for elasticSearch json build; index name and output dirs
elk_index_name = 'hash-data'
elk_index_name_session = 'session-data'
out_estack = 'out_estack'
out_pretty = 'out_pretty'

# extend the data parsing to include a second search for sig coverage
getsigdata = 'no'
# for testing to use existing pretty json output file and skip sample search
onlygetsigs = 'no'
# run a query to get the latest tag data; required periodically to ensure all tag info can be referenced
# writes to the data dir
gettagdata = 'no'
# adds exploit details to the data for exploit specific queries
# get_exploits is either set to True or False
get_exploits = False
# exploit details include fw sig db info exported from the fw and saved in the data dir
inputfile_exploits = 'exploits.csv'
# edit the query for each search
# you can copy-paste by creating a query in Autofocus and exporting using the GUI 'Export Search'
af_query = {"operator":"all","children":[{"field":"sample.malware","operator":"is","value":1},{"field":"sample.tag_group","operator":"is","value":"InternetofThingsMalware"},{"field":"sample.create_date","operator":"is after","value":["2019-01-01T00:00:00","2020-04-18T23:59:59"]}]}
# ^^^^^ placeholder comment for blank line below af query input - paste cheat
# output dir for the json and csv data
out_json = 'tag_group_stats_json'
out_csv = 'tag_group_stats_csv'
# start and end date values for time queries
start_month = 1
start_day = 28
start_year = 2020
end_month = 1
end_day = 31
end_year = 2020
date_interval = 1
# session search stall count; how many checks total same as process
stall_stop = 10