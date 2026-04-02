"""
Data Pipeline Module - ETL and data storage integration
"""

from .aws_client import AWSS3Client
from .sql_queries import RFM_CALCULATION_QUERY, RETENTION_RATE_QUERY

__all__ = ["AWSS3Client", "RFM_CALCULATION_QUERY", "RETENTION_RATE_QUERY"]
