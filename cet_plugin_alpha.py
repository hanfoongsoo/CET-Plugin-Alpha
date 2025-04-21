# CET Plugin Alpha – Structural Behavior Trajectory Module
# Author: Hanfoong Soo (2025)
# Formula: S(t) = C(t) × E(t) × T
# This structural function was originally defined by Hanfoong Soo (March 2025)

from typing import Dict

def compute_cet_score(inputs: Dict[str, float]) -> Dict[str, float]:
    """
    Compute behavioral trajectory score S(t) from inputs:
    C: Cognition level [0.0 – 1.0]
    E: Execution strength [0.0 – 1.0]
    T: Time factor (readiness or urgency modifier) [0.0 – 1.0]

    Returns:
        Dictionary containing score S(t) and basic trajectory interpretation.
    """
    C = inputs.get("C", 0.0)
    E = inputs.get("E", 0.0)
    T = inputs.get("T", 0.0)

    S = round(C * E * T, 4)

    if S >= 0.7:
        status = "🚀 High trajectory alignment"
    elif S >= 0.4:
        status = "⚠️ Partial alignment – Optimization recommended"
    else:
        status = "🔻 Off-trajectory – Immediate adjustment needed"

    return {
        "CET_Score": S,
        "Trajectory_Status": status,
        "Inputs": {"C": C, "E": E, "T": T}
    }

# Example usage
if __name__ == "__main__":
    example = compute_cet_score({"C": 0.7, "E": 0.6, "T": 0.8})
    print(example)
