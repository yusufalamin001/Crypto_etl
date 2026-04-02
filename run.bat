@echo off
docker run --dns 8.8.8.8 --env-file C:\Users\HomePC\crypto_etl\.env -v C:\Users\HomePC\crypto_etl\data:/crypto_etl/data crypto-etl:v3