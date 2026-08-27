# GALLIVIS Dataset Documentation

## Objective

The GALLIVIS dataset pipeline is designed to support pre-operative gallstone classification using multimodal clinical information.

## Target Classes

1. Cholesterol Gallstone
2. Pigment Gallstone
3. Mixed Gallstone

## Primary Imaging

Ultrasound.

## Clinical Information

Relevant demographic, symptom, laboratory, and medical-history information may be incorporated into the multimodal system.

## Optional Inputs

- MRCP
- CT
- MRI
- Raman Spectroscopy

These inputs are used only when available.

## Important Dataset Principle

A dataset must have reliable ground-truth labels for gallstone composition before it can be used to train the final three-class composition classifier.

Generic gallstone-presence datasets are not automatically suitable for this task.

## Data Locations

Raw data:
`data/raw/`

Processed data:
`data/processed/`

Metadata:
`data/metadata/`