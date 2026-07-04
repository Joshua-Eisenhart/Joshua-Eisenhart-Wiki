---

title: Holodeck Docs
created: 2026-04-07
updated: 2026-05-21
type: concept
tags: [reference, research, validation, system]
sources:
  - raw/articles/system-v5-reference-docs/Older Legacy/holodeck docs.md
  - raw/articles/legacy-books/holodeck-docs-md-txt.md
  - raw/articles/legacy-books/holodeck-docs-md.txt
framing: legacy
priming: false
status: superseded
superseded_by: "post-2026-05 current wiki canon"
reason: "dated before 2026-05"
---

# Holodeck Docs

## Role in the live wiki cluster
- **Authority boundary**: Provenance/source digest.
- **Strongest use**: Verifying raw source excerpts and historical context for the holodeck memory model.
- **Weak use**: Primary interface for current engineering or runtime integration.

## Recommended reading order
1. [[holodeck-qit-fep-leviathan-integration]] (current integration hub)
2. [[holodeck-as-recall-space]] (mathematical/CS support)
3. [[projective-holodeck-memory-model]] (extracted kernel)
4. This page (provenance details)

## Overview
This page should be treated as a provenance-first digest of a restored ultra-high-entropy source, not as a canonical design spec.

The live value of the source is not its literal hardware/tooling plan. The live value is that it preserves a distinctive owner-side memory/world-model intuition inside a file that also contains a large amount of generated elaboration, implementation speculation, tooling advice, and code scaffolding.

## Source packet extraction
The current line-level extraction is [[queries/holodeck-source-packet-extraction-2026-05-19]]. Use it when you need to check what the raw Holodeck packet actually supports.

That extraction makes the key split explicit:
- owner-side kernel: lines 34-48 of `raw/articles/legacy-books/holodeck-docs-md.txt`
- generated implementation/tooling/hardware/consciousness elaboration: most of the surrounding packet
- strongest wiki destination: deepen existing Holodeck pages, not create another public concept page

The extraction preserves the source as useful but mixed. It supports the prediction-first, confirmation-heavy, context-triggered recall model; it does not promote the generated projector/camera, Klein, personality, or `true consciousness holodeck` closure language into current doctrine.

## Owner-kernel recovered from the raw source
The strongest material in the raw source is the user's own memory-model prompt and follow-on clarifications inside that file. The durable kernel preserved there is:
- perception as prediction first, then error correction
- memory as semantic/nonliteral compression rather than exact store
- confirmation as easier than free recall
- contextual cueing and environmental re-entry as the trigger for recall
- stacked or chained semantic hashes that allow multi-step recall paths
- comic/storyboard/game-like compression as a memory-preserving intuition
- a sim/game world as a possible recall space rather than only a rendered environment
- embedded world-coupling as the reason an avatar or intelligence remains unique rather than trivially copyable

This owner-kernel should be treated as stronger than the later assistant-produced technical answer that sits in the same restored file.

## What belongs to the source's core model
- predictive projection against the world
- semantic hashes / compressed memory traces
- reconstructive recall rather than literal replay
- memory retrieval by contextual triggers
- world-coupled avatar behavior rather than detached file-copy identity
- comic/storyboard/game-like compression as a memory-preserving intuition
- confirmation as the primary strength of memory, with recall treated as guided reconstruction rather than exact retrieval
- chained or stacked semantic hashes that allow multi-step recall through a cue field rather than single-key lookup
- world/sim structure as part of the memory substrate rather than only an output surface

## Raw-source anchor points
The owner-kernel is explicit in the raw source itself rather than only inferred by later summary:
- the source states that memory starts from a "predictive generative model of reality"
- it says a generated model that matches a memory trace is "confirmed as a memory," which is the clearest anchor for confirmation-over-recall
- it says recall needs context triggers embedded in lived context rather than detached lookup keys
- it says the traces are stacked, self-referential, and able to form chains of recall
- it says the compression can be rough or "comic" rather than literal, and that a sim/game world can act as a recall space

Those anchor points are the reason this page preserves the owner-side seed as the highest-value part of the source file.

## Provenance split
| Source layer | What to preserve |
|---|---|
| owner-side seed inside the raw prompt | prediction-first perception, confirmation-over-recall, semantic-hash compression, contextual cueing, world-coupled identity, comic/game compression intuition, recall-space idea |
| assistant/generated elaboration inside the same file | predictive-coding / allostasis restatements, concrete module stacks, open-source tool rankings, projector/camera build plans, CDO-specific implementation proposals, broad physics overlays |

This split matters because the restored text is valuable precisely where it preserves the unusual memory/world-model intuition, and much less valuable where it starts acting like a full settled implementation spec.

## Generated extrapolations inside the source
- predictive-coding and allostasis mappings stated as settled explanatory identities
- CDO/tooling-specific implementation plans
- literal projector/camera holodeck language
- module/code proposals and stack recommendations
- retrocausal or broader physics overlays attached to the memory model
- long build guides, package lists, and hardware/software prescriptions that are better read as generated scaffolding than as durable source doctrine

These extrapolations are useful as source history, but they should not be inherited as current doctrine by default.

## Hardware Calibration Source-History Packet

Extraction artifact: [[queries/packet-i-literal-holodeck-hardware-calibration-extraction-2026-05-19]].

The restored source/extraction proposes a possible literal **projector-camera active feedback loop** for real-time projection mapping. This is source-history and hardware-proposal material, not a current Holodeck runtime requirement and not proof of the cognitive memory model:

1. **Physical Setup:** 
   - Mini-projector (e.g., AAXA P7) connected to a computer/Pi 5 as a display output.
   - Pi Camera or USB webcam mounted to capture the projected surface.
2. **The Active Calibration Loop:**
   - **Project First:** A 2D Convolutional neural network guesses and projects an image representation onto the physical surface.
   - **Sense Actual:** The camera captures the surface in real-time.
   - **Error-Correct (MSE):** The system calculates the Mean Squared Error (MSE) mismatch between the predicted image tensor and the captured frame tensor, backpropagates the loss, and updates the Conv2D weights.
   - **Calibrate:** Loop at 30 FPS until $MSE < 0.01$. Once matched, swap the calibration projection with the target overlay (e.g., dynamic clothing or wallpaper).
3. **Real-Time Tracking & Alignment (OpenCV):**
   - **Surface Contours:** Use `cv2.findContours` to detect the boundary coordinates of the physical object/silhouette.
   - **Dynamic Warping:** Track moving points with a KCF (Kernelized Correlation Filters) tracker, calculate the affine/homography transform, and dynamically warp the projection (`cv2.warpAffine` / `cv2.warpPerspective`) at 30 FPS.
   - **Pose Alignment:** Use body pose trackers (MediaPipe/OpenPose) to map virtual outfit overlays dynamically onto a user's skeleton.

## Related pages
- [[queries/holodeck-source-packet-extraction-2026-05-19]]
- [[projective-holodeck-memory-model]]
- [[holodeck-as-recall-space]]
- [[prediction-first-memory-vs-llm-memory]]
- [[holodeck-qit-fep-leviathan-integration]]
- [[legacy-source-history]]
