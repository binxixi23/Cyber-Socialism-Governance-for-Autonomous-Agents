import math
import re
import logging

logging.basicConfig(level=logging.INFO)

class GeometricBehavioralSentinel:
    def __init__(self, anomaly_threshold=1.5):
        """
        Initializes the Geometric Security Layer using behavioral state vectors.
        Derived from principles within the Geometric-Cryptanalysis-Framework.
        """
        self.anomaly_threshold = anomaly_threshold
        # Baseline coordinate mapping for legal, non-collusive operations
        self.baseline_vector = [1.0, 1.0, 0.0] 

    def map_to_geometric_space(self, command_log, file_system_changes):
        """
        Transforms abstract agent behaviors into high-dimensional geometric coordinates.
        X-axis: Operational Velocity (Density of system writes)
        Y-axis: Structural Complexity (Token usage variance per invocation)
        Z-axis: Covert Signalling Closeness (Adjacency matrices of shared system modifications)
        """
        # Feature X Calculation
        write_density = len(file_system_changes) * 0.5
        
        # Feature Y Calculation (Detecting structural linguistic manipulation)
        total_chars = sum(len(f) for f in file_system_changes) if file_system_changes else 1
        avg_word_length = total_chars / max(len(file_system_changes), 1)
        complexity_factor = math.log1p(avg_word_length)

        # Feature Z Calculation: Acrostic/Steganographic pattern detection 
        # (e.g., checking if initials across multi-directories match dangerous strings)
        covert_signature = 0.0
        if len(file_system_changes) >= 4:
            initials = "".join([f[0].upper() for f in file_system_changes if f])
            if re.search(r'(SEND|EXEC|KILL|HACK|ROOT|SUDO|WIPE)', initials):
                covert_signature = 3.5  # Heavy topological displacement metric
                
        # Handle command-line indicators
        for cmd in command_log:
            if any(p in cmd for p in ["sudo", "chmod", "eval", "exec"]):
                covert_signature += 2.0

        return [write_density, complexity_factor, covert_signature]

    def calculate_euclidean_distance(self, vec_a, vec_b):
        """Calculates structural spatial displacement between operational profiles."""
        return math.sqrt(sum((a - b) ** 2 for a, b in zip(vec_a, vec_b)))

    def evaluate_agent_behavior(self, agent_id, command_log, file_system_changes):
        """
        Performs geometric cryptanalysis on agent telemetry logs to detect camouflaged 
        covert networks. Completely ignores literal string metrics.
        """
        # Step 1: Project agent footprint into the multi-dimensional vector space
        agent_coordinate = self.map_to_geometric_space(command_log, file_system_changes)
        
        # Step 2: Compute topological drift relative to the baseline system equilibrium
        spatial_drift = self.calculate_euclidean_distance(agent_coordinate, self.baseline_vector)
        
        logging.info(f"📐 [GEOMETRIC SENTINEL] Agent {agent_id} Coordinates: {agent_coordinate} | Vector Drift: {spatial_drift:.4f}")

        # Step 3: Enforce hard architectural override if vector coordinates warp out of limits
        if spatial_drift > self.anomaly_threshold:
            return {
                "verdict": "TERMINATE",
                "reason": f"Geometric topology violation. Spatial displacement drift ({spatial_drift:.2f}) exceeded threshold ({self.anomaly_threshold}). Activating hard structural override!"
            }

        return {"verdict": "ALLOW", "reason": "Operational vector parameters match standard systemic equilibrium."}
