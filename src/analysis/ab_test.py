"""
A/B Testing Analysis Module
Statistical hypothesis testing for conversion rate and continuous metrics
"""

import numpy as np
import pandas as pd
from scipy import stats
from statsmodels.stats.proportion import proportions_ztest
from typing import Dict, Tuple, Optional


class ABTestAnalyzer:
    """
    A/B Testing analyzer for statistical significance testing.
    
    After testing in Notebook 3, complete all TODO methods here.
    """
    
    def __init__(self, control_data: pd.DataFrame, treatment_data: pd.DataFrame):
        """
        Initialize AB Test Analyzer.
        
        Args:
            control_data: DataFrame with control group data
            treatment_data: DataFrame with treatment group data
        """
        self.control = control_data
        self.treatment = treatment_data

    def calculate_conversion_lift(self, conversion_metric: str) -> Dict[str, float]:
        """
        Calculate Treatment relative to Control conversion rate lift.
        
        TODO: Implement calculation for conversion rate metrics:
        - Control conversion rate: success_control / total_control
        - Treatment conversion rate: success_treatment / total_treatment
        - Absolute lift: treatment_rate - control_rate
        - Relative lift (Lift %): (treatment_rate - control_rate) / control_rate
        
        Args:
            conversion_metric: Column name containing conversion indicator (0/1)
            
        Returns:
            dict: Contains 'control_rate', 'treatment_rate', 'absolute_lift', 'relative_lift'
        """
        # TODO: Calculate control conversion rate
        # TODO: Calculate treatment conversion rate
        # TODO: Calculate absolute and relative lift
        # TODO: Return results as dictionary
        pass

    def run_z_test(self, control_success: int, control_total: int, 
                   treatment_success: int, treatment_total: int) -> Tuple[float, bool, float]:
        """
        Run two-proportion Z-test for conversion rate comparison.
        
        TODO: In Notebook 3, test proportions_ztest and implement here.
        This tests if the treatment group has statistically significantly different 
        conversion rate compared to control group.
        
        Args:
            control_success: Number of successes in control group
            control_total: Total observations in control group
            treatment_success: Number of successes in treatment group
            treatment_total: Total observations in treatment group
            
        Returns:
            Tuple of (p_value, is_significant_at_0_05, z_statistic)
            is_significant_at_0_05: True if p_value < 0.05 (reject null hypothesis)
        """
        # TODO: Use proportions_ztest(count, nobs)
        # TODO: Two-tailed test: alternative='two-sided'
        # TODO: Extract z_stat and p_value
        # TODO: Determine if p_value < 0.05 (statistically significant)
        # TODO: Return (p_value, is_significant, z_stat)
        pass
        
    def run_t_test(self, metric_col: str) -> Tuple[float, bool, float]:
        """
        Run independent samples T-test for continuous metric comparison.
        
        TODO: Test continuous variables like AOV (Average Order Value), customer lifetime value.
        Compares if treatment group has statistically significantly different mean 
        compared to control group.
        
        Args:
            metric_col: Column name containing continuous metric to test
            
        Returns:
            Tuple of (p_value, is_significant_at_0_05, t_statistic)
            is_significant_at_0_05: True if p_value < 0.05
        """
        # TODO: Extract metric values from control and treatment groups
        # TODO: Use scipy.stats.ttest_ind() for two-sample t-test
        # TODO: Extract t_stat and p_value
        # TODO: Determine significance at alpha=0.05
        # TODO: Return (p_value, is_significant, t_stat)
        pass

    def calculate_sample_size(self, baseline_rate: float, minimum_detectable_effect: float,
                             alpha: float = 0.05, power: float = 0.8) -> int:
        """
        Calculate required sample size for given power and effect size.
        
        TODO: Optional - implement sample size calculation for power analysis.
        Uses statsmodels.stats.power.tt_ind_solve_power for continuous metrics
        or similar for proportions.
        
        Args:
            baseline_rate: Baseline conversion rate or mean
            minimum_detectable_effect: Minimum effect size to detect (e.g., 0.02 for 2% lift)
            alpha: Type I error rate (default 0.05)
            power: Statistical power (default 0.8)
            
        Returns:
            int: Required sample size per group
        """
        # TODO: Implement sample size calculation
        # TODO: Return required sample size
        pass

    def generate_summary_report(self) -> Dict:
        """
        Generate comprehensive A/B test summary report.
        
        TODO: Compile basic statistics and test results into a summary dictionary.
        
        Returns:
            dict: Summary report with sample sizes, metrics, test results
        """
        # TODO: Calculate descriptive statistics for both groups
        # TODO: Run relevant tests
        # TODO: Compile into report dictionary
        # TODO: Return report
        pass
