#!/bin/bash
echo "Building and starting FluffStack cloud..."
docker-compose up -d --build
docker ps