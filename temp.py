import time
t1 = time.time()
import eppy
fname = "/Users/santosh/Dropbox/coolshadow_dropbox/HOK_O_Street/simulation/title-24/ostreet/epyyruns/190731_T24_07ap.idf"
weatherfile = "/Users/santosh/Dropbox/coolshadow_dropbox/HOK_O_Street/simulation/weather_files/USA_CA_Sacramento.Exec.AP.724830_TMY3/USA_CA_Sacramento.Exec.AP.724830_TMY3.epw"
idf = eppy.openidf(fname, epw=weatherfile)
import witheppy.runner
witheppy.runner.eplaunch_run(idf)
t2 = time.time()

print t2 - t1
