@echo off
docker run --env-file C:\Users\HomePC\crypto_etl\.env -v C:\Users\HomePC\crypto_etl\data:/crypto_etl/data crypto-etl:v1