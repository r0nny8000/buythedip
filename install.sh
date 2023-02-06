#!/bin/bash

echo 'building and installing'

poetry build
pip install dist/crypto-0.1.0.tar.gz