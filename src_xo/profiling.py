import profile
import pstats

profile.run('import Foodforce2; Foodforce2.main()', 'profile.tmp')
       
p = pstats.Stats('profile.tmp')
p.sort_stats('cumulative').print_stats(1000)
       