# LinkedIn carousel operator brief

**Asset:** launch/OCF-V1-LinkedIn-Carousel-3page.pdf  
**Builder:** launch/build_linkedin_carousel.py  
**Format:** 3-page portrait PDF, 1080 × 1350 points per page.  
**Companion copy:** launch/07-linkedin-post.md

Upload the PDF as a LinkedIn document carousel, or upload the three page PNGs (`launch/carousel-page-1.png`, `launch/carousel-page-2.png`, `launch/carousel-page-3.png`, each 1080 × 1350) as a native LinkedIn image carousel if document upload is unavailable or lower fidelity. Publish last, after the DOI-aware posts in the launch order; keep the rollout staggered and do not spray all channels on Day 1. The operator uploads and posts manually; there is no auto-post step.

## Page-by-page

1. **The result.** Lead with 5.29M local output tokens and 224 coding sessions. Show the $0 local API charge and the 83.6 GB model / 16 GB VRAM hardware envelope. The small qualifier names host RAM and NVMe offload so the page does not imply the full model resides in GPU memory.
2. **The graphs.** Compare coding output with compaction output, then show the five cloud list-rate counterfactuals. Keep the $0 local API and 94.79% cache-read callouts visible. The graph labels identify the prices as counterfactuals, not bills.
3. **Links and how to read.** Give clickable links to the repository, v1.2.0 release, Zenodo concept DOI and record, full token report, and paper Section 5.7. A closing note says the cloud comparison is not an invoice, the measurement views are non-additive, and the DOI identifies the Zenodo concept record.

The figures and wording come from launch/_linkedin_seed.json. The builder embeds charts in the PDF and also writes the three page PNGs listed above for native LinkedIn image upload.
