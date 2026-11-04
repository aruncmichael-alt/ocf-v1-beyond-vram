# Operational Boundaries and Limitations

Extracted from the OCF V1 case study by Arun C Michael.

## 6. Operational Boundaries and Scope Conditions

1. **Single-Workstation Hardware Envelope:** Measurements reflect an NVIDIA RTX 5080 (16,303 MiB) paired with a high-RAM host and internal NVMe SSD. Performance scales with host DRAM capacity, memory bus bandwidth, PCIe lane allocation, and NVMe random-read latency.
2. **End-to-End Stack Comparison:** The coding screen evaluates deployed operational configurations (`Ollama` dense vs. `Strata` sparse with `MTP`), reflecting real-world workstation tooling rather than isolated theoretical weight comparisons.
3. **Platform-Specific Concurrency Primitives:** The `OCF V1` PowerShell runners use Windows named mutexes, `.NET` `ProcessStartInfo` argument quoting, and Win32 process creation timestamps. Linux and macOS ports require adapting the lock layer to `flock`/`fcntl` and `/proc/<pid>/stat` start-time ticks.
4. **Out-of-Scope Hardware Telemetry:** Wall-socket AC power draw, multi-hour thermal equilibrium curves, and NVMe SSD write endurance (TBW) were outside the scope of this software-integration study (`NOT MEASURED`).

---
