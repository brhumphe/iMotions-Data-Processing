import utils
from DataProcess.filter import Filter
from DataProcess.sensors import Affdex

path = "data/adidas runners S2/001_307.txt"
print(utils.read_cols(path))
print(utils.read_events(path))

affdex_filter = Filter([Affdex])
data = utils.open_file(path, ['AffRaw'])
print(affdex_filter.filter(next(data)))
