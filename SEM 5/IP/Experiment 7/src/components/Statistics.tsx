import React from 'react';
import { FormStats } from '../types';

interface StatisticsProps {
  formStats: FormStats[];
  submissionCount: number;
  currentUser?: string;
}

const Statistics: React.FC<StatisticsProps> = ({ 
  formStats, 
  submissionCount, 
  currentUser 
}) => {
  // Calculate statistics using various operators
  const totalValidations = formStats.reduce((sum, stat) => sum + stat.validations, 0);
  const totalErrors = formStats.reduce((sum, stat) => sum + stat.errors, 0);
  const successRate = totalValidations > 0 
    ? ((totalValidations - totalErrors) / totalValidations * 100).toFixed(1) 
    : '100';

  return (
    <div className="statistics">
      <h3>📊 Form Statistics</h3>
      <div className="stats-grid">
        <div className="stat-item">
          <h4>Total Submissions</h4>
          <p>{submissionCount}</p>
        </div>
        <div className="stat-item">
          <h4>Total Validations</h4>
          <p>{totalValidations}</p>
        </div>
        <div className="stat-item">
          <h4>Total Errors</h4>
          <p>{totalErrors}</p>
        </div>
        <div className="stat-item">
          <h4>Success Rate</h4>
          <p>{successRate}%</p>
        </div>
        {currentUser && (
          <div className="stat-item">
            <h4>Current User</h4>
            <p>{currentUser}</p>
          </div>
        )}
      </div>
    </div>
  );
};

export default Statistics;
