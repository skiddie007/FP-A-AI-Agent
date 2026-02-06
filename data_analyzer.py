import pandas as pd
import numpy as np
from typing import Dict, List, Any

class DataAnalyzer:
    def __init__(self, df: pd.DataFrame):
        self.df = df
        
    def get_summary_statistics(self) -> Dict[str, Any]:
        """Generate comprehensive summary statistics"""
        summary = {}
        
        # Basic info
        summary['total_rows'] = len(self.df)
        summary['total_columns'] = len(self.df.columns)
        summary['column_names'] = list(self.df.columns)
        
        # Numeric columns analysis
        numeric_cols = self.df.select_dtypes(include=[np.number]).columns.tolist()
        if numeric_cols:
            summary['numeric_columns'] = numeric_cols
            summary['numeric_stats'] = {}
            
            for col in numeric_cols:
                summary['numeric_stats'][col] = {
                    'mean': float(self.df[col].mean()),
                    'median': float(self.df[col].median()),
                    'std': float(self.df[col].std()),
                    'min': float(self.df[col].min()),
                    'max': float(self.df[col].max()),
                    'sum': float(self.df[col].sum()),
                    'missing_values': int(self.df[col].isna().sum())
                }
        
        # Categorical columns analysis
        categorical_cols = self.df.select_dtypes(include=['object']).columns.tolist()
        if categorical_cols:
            summary['categorical_columns'] = categorical_cols
            summary['categorical_stats'] = {}
            
            for col in categorical_cols:
                value_counts = self.df[col].value_counts().head(10)
                summary['categorical_stats'][col] = {
                    'unique_values': int(self.df[col].nunique()),
                    'most_common': value_counts.to_dict(),
                    'missing_values': int(self.df[col].isna().sum())
                }
        
        return summary
    
    def get_correlations(self) -> Dict[str, Any]:
        """Calculate correlations between numeric columns"""
        numeric_df = self.df.select_dtypes(include=[np.number])
        
        if len(numeric_df.columns) < 2:
            return {'message': 'Need at least 2 numeric columns for correlation analysis'}
        
        corr_matrix = numeric_df.corr()
        
        # Find strong correlations
        strong_correlations = []
        for i in range(len(corr_matrix.columns)):
            for j in range(i+1, len(corr_matrix.columns)):
                corr_value = corr_matrix.iloc[i, j]
                if abs(corr_value) > 0.5:
                    strong_correlations.append({
                        'column1': corr_matrix.columns[i],
                        'column2': corr_matrix.columns[j],
                        'correlation': float(corr_value)
                    })
        
        return {
            'correlation_matrix': corr_matrix.to_dict(),
            'strong_correlations': strong_correlations
        }
    
    def get_trends_and_patterns(self) -> Dict[str, Any]:
        """Identify trends and patterns in the data"""
        patterns = {}
        
        numeric_cols = self.df.select_dtypes(include=[np.number]).columns.tolist()
        
        for col in numeric_cols:
            # Calculate growth/decline if there's a sequence
            if len(self.df) > 1:
                first_value = self.df[col].iloc[0]
                last_value = self.df[col].iloc[-1]
                
                if first_value != 0:
                    change_pct = ((last_value - first_value) / first_value) * 100
                    patterns[col] = {
                        'first_value': float(first_value),
                        'last_value': float(last_value),
                        'change_percentage': float(change_pct),
                        'trend': 'increasing' if change_pct > 5 else 'decreasing' if change_pct < -5 else 'stable'
                    }
        
        return patterns
    
    def query_data(self, question: str) -> str:
        """Answer questions about the data"""
        question_lower = question.lower()
        
        # Handle common questions
        if 'total' in question_lower or 'sum' in question_lower:
            numeric_cols = self.df.select_dtypes(include=[np.number]).columns.tolist()
            if numeric_cols:
                totals = {col: float(self.df[col].sum()) for col in numeric_cols}
                return f"Column totals: {totals}"
        
        if 'average' in question_lower or 'mean' in question_lower:
            numeric_cols = self.df.select_dtypes(include=[np.number]).columns.tolist()
            if numeric_cols:
                averages = {col: float(self.df[col].mean()) for col in numeric_cols}
                return f"Column averages: {averages}"
        
        if 'max' in question_lower or 'highest' in question_lower:
            numeric_cols = self.df.select_dtypes(include=[np.number]).columns.tolist()
            if numeric_cols:
                maximums = {col: float(self.df[col].max()) for col in numeric_cols}
                return f"Maximum values: {maximums}"
        
        if 'min' in question_lower or 'lowest' in question_lower:
            numeric_cols = self.df.select_dtypes(include=[np.number]).columns.tolist()
            if numeric_cols:
                minimums = {col: float(self.df[col].min()) for col in numeric_cols}
                return f"Minimum values: {minimums}"
        
        if 'count' in question_lower or 'how many' in question_lower:
            return f"Total rows: {len(self.df)}, Total columns: {len(self.df.columns)}"
        
        return "I can help with questions about totals, averages, max/min values, counts, and trends in your data."
    
    def get_financial_insights(self) -> Dict[str, Any]:
        """Generate FP&A specific insights"""
        insights = {}
        
        # Look for common financial columns
        financial_keywords = ['revenue', 'sales', 'cost', 'expense', 'profit', 'margin', 'ebitda', 'cash', 'budget', 'actual', 'variance']
        
        found_columns = []
        for col in self.df.columns:
            col_lower = col.lower()
            for keyword in financial_keywords:
                if keyword in col_lower:
                    found_columns.append(col)
                    break
        
        if found_columns:
            insights['financial_columns_detected'] = found_columns
            
            for col in found_columns:
                if self.df[col].dtype in [np.int64, np.float64]:
                    insights[col] = {
                        'total': float(self.df[col].sum()),
                        'average': float(self.df[col].mean()),
                        'trend': 'positive' if self.df[col].sum() > 0 else 'negative'
                    }
        
        return insights
