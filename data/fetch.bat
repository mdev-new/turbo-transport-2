@echo off

echo Stahuji...

rem Vlaky?
curl -O https://portal.cisjr.cz/pub/netex/NeTEx_GVD2024.zip

rem Trolejbusy, tramvaje, lanovky
curl -O https://portal.cisjr.cz/pub/netex/NeTEx_DrahyMestske.zip

rem Linkove autobusy
curl -O https://portal.cisjr.cz/pub/netex/NeTEx_VerejnaLinkovaDoprava.zip

rem Mapa
curl -O https://download.geofabrik.de/europe/czech-republic-latest.osm.bz2
