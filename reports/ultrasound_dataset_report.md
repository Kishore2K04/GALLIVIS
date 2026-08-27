# GALLIVIS Ultrasound Dataset Report

## Dataset

UIdataGB / Gallstones subset

## Purpose

This dataset is being used for ultrasound image pipeline development.

It is not being treated as ground truth for Cholesterol/Pigment/Mixed gallstone composition.

## Image Count

Expected extracted images:

1326

## Validation

Image validity is checked using the GALLIVIS image validation pipeline.

## Analysis

The dataset analysis pipeline records:

- Total images
- Image dimensions
- Image formats
- Corrupted files
- Perceptual duplicate groups

## Ground Truth

The dataset does not provide verified Cholesterol/Pigment/Mixed composition labels.

Therefore, composition labels must not be inferred from these images.

## Processing Status

Raw images remain unchanged.

Further preprocessing will be performed into:

`data/processed/ultrasound/`