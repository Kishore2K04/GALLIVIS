# GALLIVIS Data Integrity Rules

## Rule 1 — No fabricated labels

GALLIVIS must never infer a Cholesterol, Pigment, or Mixed label simply from an ultrasound image unless a validated ground-truth source supports the label.

## Rule 2 — Preserve patient identity within the dataset

Images belonging to the same patient must remain associated with the same patient identifier.

## Rule 3 — Patient-level splitting

Training, validation, and testing splits must be performed at the patient level whenever patient identifiers are available.

## Rule 4 — Separate auxiliary datasets

Datasets that contain gallstone images but do not contain composition labels may be used for:

- preprocessing
- image-quality testing
- gallstone detection
- visualization
- transfer-learning experiments

They must not automatically be treated as Cholesterol/Pigment/Mixed ground truth.

## Rule 5 — Ground-truth source must be recorded

Every final composition label must record the method/source used to establish the label.

Examples:

- chemical analysis
- FTIR
- validated spectroscopy
- documented pathological/clinical reference

## Rule 6 — Optional modalities

MRCP, CT, MRI and Raman spectroscopy are optional inputs.

GALLIVIS must not require these modalities when they are unavailable.

## Rule 7 — Pre-operative focus

GALLIVIS is designed for pre-operative decision support.

Post-operative information is not an input requirement for the deployed system.