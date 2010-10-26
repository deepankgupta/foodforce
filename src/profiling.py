import profile
import pstats

profile.run('import Foodforce2; Foodforce2.main()', 'profile')
       
p = pstats.Stats('profile')
p.sort_stats('cumulative').print_stats(1000)
