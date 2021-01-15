import converters
print(converters.kg_to_lbs(200))
# or
from converters import kg_to_lbs
print(kg_to_lbs(200))


from utils import find_max
print(find_max([100, 200, 3, 5]))
# or
import utils as ut
print(ut.find_max([100, 200, 3, 5]))
