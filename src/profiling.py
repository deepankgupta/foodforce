import profile
import pstats

profile.run('import Foodforce2; Foodforce2.main()', 'profile')
       
p = pstats.Stats('profile')
p.sort_stats('time').print_stats(1000)
