@echo off
color 0B
title Yildiz Avcisi - SQL Sunucusu

echo ==============================================
echo        SQL SUNUCUSU BASLATILIYOR 
echo ==============================================
echo.

echo [1/2] Gerekli Python paketleri kuruluyor...
python -m pip install flask

echo.
echo [2/2] Sunucu aktif ediliyor...
echo Tarayicinizda oyun birazdan acilacaktir.
echo Kapatmak istediginizde bu pencereyi carpidan kapatabilirsiniz.
echo.

start http://127.0.0.1:5000
python server.py
pause
