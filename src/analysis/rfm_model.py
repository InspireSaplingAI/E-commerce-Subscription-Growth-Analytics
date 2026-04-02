"""
RFM (Recency, Frequency, Monetary) Model Module
Customer segmentation based on purchase behavior
"""

import pandas as pd
import numpy as np
from typing import Dict, List


class RFMModel:
    """
    RFM Model for customer segmentation.
    
    RFM segments customers based on:
    - Recency: How recently they made a purchase
    - Frequency: How often they purchase
    - Monetary: How much they spend
    """
    
    def __init__(self, df: pd.DataFrame):
        """
        Initialize RFM Model.
        
        Args:
            df: DataFrame with RFM scores (columns: customer_id, recency_score, frequency_score, monetary_score)
        """
        self.df = df
        self.segments = None

    def calculate_rfm_scores(self, recency_col: str, frequency_col: str, 
                            monetary_col: str, n_tiles: int = 5) -> pd.DataFrame:
        """
        Calculate RFM scores from raw data using NTILE ranking.
        
        TODO: Implement NTILE-based scoring that creates quintiles (1-5) for each dimension.
        
        Args:
            recency_col: Column name for recency (days since last purchase)
            frequency_col: Column name for purchase frequency
            monetary_col: Column name for total monetary value
            n_tiles: Number of tiles for NTILE (default 5 for quintiles)
            
        Returns:
            pd.DataFrame: DataFrame with R_score, F_score, M_score columns
        """
        # TODO: Use pandas rank or scipy.stats.rankdata to create NTILE scores
        # TODO: For Recency: lower (more recent) = higher score
        # TODO: For Frequency and Monetary: higher values = higher score
        # TODO: Return DataFrame with R_score (1-5), F_score (1-5), M_score (1-5)
        pass

    def segment_customers(self, r_score: str, f_score: str, m_score: str) -> pd.DataFrame:
        """
        Segmentize customers based on RFM scores into meaningful groups.
        
        TODO: Define customer segments based on RFM score combinations:
        - Champions: High R, F, M
        - Loyal Customers: High F, M
        - At-Risk: Low R (haven't purchased recently)
        - Need Attention: Medium scores
        - Lost: Very low R, F, M
        
        Args:
            r_score: Column name for Recency score
            f_score: Column name for Frequency score
            m_score: Column name for Monetary score
            
        Returns:
            pd.DataFrame: Original data with added 'segment' column
        """
        # TODO: Define segment logic based on R, F, M combinations
        # TODO: Create new column 'segment' with segment labels
        # TODO: Return segmented DataFrame
        pass

    def get_segment_summary(self, segment_col: str) -> pd.DataFrame:
        """
        Get summary statistics for each segment.
        
        Args:
            segment_col: Column name containing segment labels
            
        Returns:
            pd.DataFrame: Summary with count, average RFM scores per segment
        """
        # TODO: Group by segment
        # TODO: Calculate count, average R/F/M scores per segment
        # TODO: Return summary DataFrame
        pass

    def segment_statistics(self) -> Dict:
        """
        Provide detailed statistics for each customer segment.
        
        TODO: Generate segment-level insights.
        
        Returns:
            dict: Dictionary with segment names as keys, statistics as values
        """
        # TODO: For each segment, calculate size, average values, etc.
        # TODO: Return as dictionary
        pass
