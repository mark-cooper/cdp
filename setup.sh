#!/bin/bash

mkdir -p data/assessments
mkdir -p data/ead
mkdir -p data/import
mkdir -p data/resources

rm -f data/assessments/*
rm -f data/ead/*
rm -f data/import/*
rm -f data/resources/*

rm -f *.csv
rm -f *.bak
rm -f sql/wip.sql
