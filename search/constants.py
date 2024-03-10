# generate this with overpass turbo (export->raw data from overpass api->copy link addr)
# OVERPASS_REQUEST = "https://overpass-api.de/api/interpreter?data=%5Bout%3Ajson%5D%5Btimeout%3A25%5D%3B%0A%0A%28%0A%20%20nwr%5B%22highway%22%3D%22footway%22%5D%2850.01336521151482%2C15.712336264218326%2C50.055706016646624%2C15.81911328580062%29%3B%0A%20%20nwr%5B%22type%22%21%3D%22multipolygon%22%5D%5B%22highway%22%3D%22pedestrian%22%5D%2850.01336521151482%2C15.712336264218326%2C50.055706016646624%2C15.81911328580062%29%3B%0A%20%20nwr%5B%22highway%22%3D%22path%22%5D%2850.01336521151482%2C15.712336264218326%2C50.055706016646624%2C15.81911328580062%29%3B%0A%20%20nwr%5B%22access%22%21%3D%22private%22%5D%5B%22highway%22%3D%22service%22%5D%2850.01336521151482%2C15.712336264218326%2C50.055706016646624%2C15.81911328580062%29%3B%0A%20%20nwr%5B%22highway%22%3D%22residential%22%5D%2850.01336521151482%2C15.712336264218326%2C50.055706016646624%2C15.81911328580062%29%3B%0A%20%20nwr%5B%22highway%22%3D%22living_street%22%5D%2850.01336521151482%2C15.712336264218326%2C50.055706016646624%2C15.81911328580062%29%3B%0A%20%20nwr%5B%22highway%22%3D%22steps%22%5D%2850.01336521151482%2C15.712336264218326%2C50.055706016646624%2C15.81911328580062%29%3B%0A%20%20nwr%5B%22highway%22%3D%22sidewalk%22%5D%2850.01336521151482%2C15.712336264218326%2C50.055706016646624%2C15.81911328580062%29%3B%0A%20%20nwr%5B%22highway%22%3D%22track%22%5D%2850.01336521151482%2C15.712336264218326%2C50.055706016646624%2C15.81911328580062%29%3B%0A%20%20%2F%2Fnwr%5B%22highway%22%3D%22crossing%22%5D%2850.01336521151482%2C15.712336264218326%2C50.055706016646624%2C15.81911328580062%29%3B%0A%20%20nwr%5B%22highway%22%3D%22cycleway%22%5D%2850.01336521151482%2C15.712336264218326%2C50.055706016646624%2C15.81911328580062%29%3B%0A%20%20%2F%2Fnwr%5B%22route%22%3D%22foot%22%5D%2850.01336521151482%2C15.712336264218326%2C50.055706016646624%2C15.81911328580062%29%3B%0A%29%3B%0Aout%20geom%3B%20%2F%2F%20print%20results%0A%0A%28%0Anwr%5B%22type%22%3D%22route%22%5D%5B%22route%22~%22bus%22%5D%2850.01336521151482%2C15.712336264218326%2C50.055706016646624%2C15.81911328580062%29%3B%0A%29%3B%0Aout%20geom%3B%0A%0A%28%0Anwr%5B%22public_transport%22%5D%5B%22bus%22%3D%22yes%22%5D%2850.01336521151482%2C15.712336264218326%2C50.055706016646624%2C15.81911328580062%29%3B%0A%29%3B%0Aout%20geom%3B%0A"

OVERPASS_REQUEST="https://overpass-api.de/api/interpreter?data=%5Bout%3Ajson%5D%5Btimeout%3A25%5D%3B%0A%0A%28%0A%20%20nwr%5B%22highway%22%3D%22footway%22%5D%2850.03262443156067%2C15.786323146619964%2C50.0378204786263%2C15.794412178472827%29%3B%0A%20%20nwr%5B%22type%22%21%3D%22multipolygon%22%5D%5B%22highway%22%3D%22pedestrian%22%5D%2850.03262443156067%2C15.786323146619964%2C50.0378204786263%2C15.794412178472827%29%3B%0A%20%20nwr%5B%22highway%22%3D%22path%22%5D%2850.03262443156067%2C15.786323146619964%2C50.0378204786263%2C15.794412178472827%29%3B%0A%20%20nwr%5B%22access%22%21%3D%22private%22%5D%5B%22highway%22%3D%22service%22%5D%2850.03262443156067%2C15.786323146619964%2C50.0378204786263%2C15.794412178472827%29%3B%0A%20%20nwr%5B%22highway%22%3D%22residential%22%5D%2850.03262443156067%2C15.786323146619964%2C50.0378204786263%2C15.794412178472827%29%3B%0A%20%20nwr%5B%22highway%22%3D%22living_street%22%5D%2850.03262443156067%2C15.786323146619964%2C50.0378204786263%2C15.794412178472827%29%3B%0A%20%20nwr%5B%22highway%22%3D%22steps%22%5D%2850.03262443156067%2C15.786323146619964%2C50.0378204786263%2C15.794412178472827%29%3B%0A%20%20nwr%5B%22highway%22%3D%22sidewalk%22%5D%2850.03262443156067%2C15.786323146619964%2C50.0378204786263%2C15.794412178472827%29%3B%0A%20%20nwr%5B%22highway%22%3D%22track%22%5D%2850.03262443156067%2C15.786323146619964%2C50.0378204786263%2C15.794412178472827%29%3B%0A%20%20%2F%2Fnwr%5B%22highway%22%3D%22crossing%22%5D%2850.03262443156067%2C15.786323146619964%2C50.0378204786263%2C15.794412178472827%29%3B%0A%20%20nwr%5B%22highway%22%3D%22cycleway%22%5D%2850.03262443156067%2C15.786323146619964%2C50.0378204786263%2C15.794412178472827%29%3B%0A%20%20%2F%2Fnwr%5B%22route%22%3D%22foot%22%5D%2850.03262443156067%2C15.786323146619964%2C50.0378204786263%2C15.794412178472827%29%3B%0A%29%3B%0Aout%20geom%3B%20%2F%2F%20print%20results%0A%0A%28%0Anwr%5B%22type%22%3D%22route%22%5D%5B%22route%22~%22bus%22%5D%2850.03262443156067%2C15.786323146619964%2C50.0378204786263%2C15.794412178472827%29%3B%0A%29%3B%0Aout%20geom%3B%0A%0A%28%0Anwr%5B%22public_transport%22%5D%5B%22bus%22%3D%22yes%22%5D%2850.03262443156067%2C15.786323146619964%2C50.0378204786263%2C15.794412178472827%29%3B%0A%29%3B%0Aout%20geom%3B%0A"