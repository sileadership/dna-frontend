from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np
from datetime import datetime


app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

class BusinessAnalyzer:
    def __init__(self):
        self.industry_benchmarks = {
            'technology': {
                'avg_revenue_growth': 25,
                'avg_profit_margin': 22,
                'avg_employee_productivity': 2500000,
                'avg_working_capital_ratio': 2.5,
                'rd_investment_ratio': 15
            },
            'retail': {
                'avg_revenue_growth': 12,
                'avg_profit_margin': 8,
                'avg_employee_productivity': 1200000,
                'avg_working_capital_ratio': 1.8,
                'rd_investment_ratio': 5
            },
            'manufacturing': {
                'avg_revenue_growth': 15,
                'avg_profit_margin': 12,
                'avg_employee_productivity': 1800000,
                'avg_working_capital_ratio': 2.0,
                'rd_investment_ratio': 8
            },
            'fmcg': {
                'avg_revenue_growth': 18,
                'avg_profit_margin': 15,
                'avg_employee_productivity': 2000000,
                'avg_working_capital_ratio': 1.5,
                'rd_investment_ratio': 6
            },
            'logistics': {
                'avg_revenue_growth': 14,
                'avg_profit_margin': 11,
                'avg_employee_productivity': 1700000,
                'avg_working_capital_ratio': 1.9,
                'rd_investment_ratio': 6
            },
            'healthcare': {
                'avg_revenue_growth': 14,
                'avg_profit_margin': 18,
                'avg_employee_productivity': 2200000,
                'avg_working_capital_ratio': 2.2,
                'rd_investment_ratio': 12
            },
            'financial': {
                'avg_revenue_growth': 16,
                'avg_profit_margin': 25,
                'avg_employee_productivity': 3000000,
                'avg_working_capital_ratio': 1.6,
                'rd_investment_ratio': 8
            },
            'telecommunications': {
                'avg_revenue_growth': 20,
                'avg_profit_margin': 20,
                'avg_employee_productivity': 2800000,
                'avg_working_capital_ratio': 2.1,
                'rd_investment_ratio': 10
            },
            'energy': {
                'avg_revenue_growth': 10,
                'avg_profit_margin': 15,
                'avg_employee_productivity': 2600000,
                'avg_working_capital_ratio': 2.3,
                'rd_investment_ratio': 7
            },
            'automotive': {
                'avg_revenue_growth': 13,
                'avg_profit_margin': 10,
                'avg_employee_productivity': 2100000,
                'avg_working_capital_ratio': 1.9,
                'rd_investment_ratio': 9
            },
            'pharmaceuticals': {
                'avg_revenue_growth': 22,
                'avg_profit_margin': 24,
                'avg_employee_productivity': 2700000,
                'avg_working_capital_ratio': 2.4,
                'rd_investment_ratio': 18
            },
            'real_estate': {
                'avg_revenue_growth': 11,
                'avg_profit_margin': 20,
                'avg_employee_productivity': 1900000,
                'avg_working_capital_ratio': 1.7,
                'rd_investment_ratio': 3
            },
            'media_entertainment': {
                'avg_revenue_growth': 17,
                'avg_profit_margin': 16,
                'avg_employee_productivity': 2300000,
                'avg_working_capital_ratio': 1.8,
                'rd_investment_ratio': 8
            },
            'agriculture': {
                'avg_revenue_growth': 8,
                'avg_profit_margin': 12,
                'avg_employee_productivity': 1500000,
                'avg_working_capital_ratio': 1.9,
                'rd_investment_ratio': 4
            },
            'aerospace_defense': {
                'avg_revenue_growth': 12,
                'avg_profit_margin': 16,
                'avg_employee_productivity': 2400000,
                'avg_working_capital_ratio': 2.2,
                'rd_investment_ratio': 14
            },
            'biotechnology': {
                'avg_revenue_growth': 28,
                'avg_profit_margin': 20,
                'avg_employee_productivity': 2900000,
                'avg_working_capital_ratio': 2.6,
                'rd_investment_ratio': 20
            },
            'chemicals': {
                'avg_revenue_growth': 9,
                'avg_profit_margin': 14,
                'avg_employee_productivity': 2000000,
                'avg_working_capital_ratio': 2.0,
                'rd_investment_ratio': 8
            },
            'construction': {
                'avg_revenue_growth': 10,
                'avg_profit_margin': 11,
                'avg_employee_productivity': 1600000,
                'avg_working_capital_ratio': 1.7,
                'rd_investment_ratio': 3
            },
            'education': {
                'avg_revenue_growth': 7,
                'avg_profit_margin': 10,
                'avg_employee_productivity': 1300000,
                'avg_working_capital_ratio': 1.5,
                'rd_investment_ratio': 5
            },
            'hospitality': {
                'avg_revenue_growth': 11,
                'avg_profit_margin': 9,
                'avg_employee_productivity': 1400000,
                'avg_working_capital_ratio': 1.4,
                'rd_investment_ratio': 2
            },
            'mining': {
                'avg_revenue_growth': 8,
                'avg_profit_margin': 13,
                'avg_employee_productivity': 2200000,
                'avg_working_capital_ratio': 2.1,
                'rd_investment_ratio': 5
            }
        }
       
        self.risk_profiles = {
            'technology': {'market': 'High', 'regulatory': 'Medium', 'operational': 'Low'},
            'retail': {'market': 'Medium', 'regulatory': 'Low', 'operational': 'High'},
            'manufacturing': {'market': 'Medium', 'regulatory': 'High', 'operational': 'High'},
            'fmcg': {'market': 'Low', 'regulatory': 'Medium', 'operational': 'Medium'},
            'healthcare': {'market': 'Low', 'regulatory': 'High', 'operational': 'Medium'},
            'logistics': {'market': 'Medium', 'regulatory': 'Medium', 'operational': 'High'},
            'financial': {'market': 'High', 'regulatory': 'High', 'operational': 'Medium'},
            'telecommunications': {'market': 'Medium', 'regulatory': 'High', 'operational': 'Medium'},
            'energy': {'market': 'High', 'regulatory': 'High', 'operational': 'High'},
            'automotive': {'market': 'High', 'regulatory': 'High', 'operational': 'High'},
            'pharmaceuticals': {'market': 'Medium', 'regulatory': 'High', 'operational': 'Medium'},
            'real_estate': {'market': 'Medium', 'regulatory': 'Medium', 'operational': 'Low'},
            'media_entertainment': {'market': 'High', 'regulatory': 'Medium', 'operational': 'Low'},
            'agriculture': {'market': 'Medium', 'regulatory': 'Medium', 'operational': 'High'},
            'aerospace_defense': {'market': 'Medium', 'regulatory': 'High', 'operational': 'High'},
            'biotechnology': {'market': 'High', 'regulatory': 'High', 'operational': 'Medium'},
            'chemicals': {'market': 'Medium', 'regulatory': 'High', 'operational': 'High'},
            'construction': {'market': 'Medium', 'regulatory': 'Medium', 'operational': 'High'},
            'education': {'market': 'Low', 'regulatory': 'Medium', 'operational': 'Low'},
            'hospitality': {'market': 'High', 'regulatory': 'Medium', 'operational': 'Medium'},
            'mining': {'market': 'High', 'regulatory': 'High', 'operational': 'High'}
        }

    def analyze_company(self, data):
        try:
            financial = self.analyze_financials(data)
            market = self.analyze_market_position(data)
            growth = self.analyze_growth(data)
            risk = self.analyze_risk(data, financial)
            swot = self.generate_swot(financial, market, growth)
            recommendations = self.generate_recommendations(financial, market, growth, risk, data['industry'].lower())
            compliance = self.check_compliance(data['industry'].lower(), financial)

            return {
                'company_name': data['company_name'],
                'analysis': {
                    'financial': financial,
                    'market': market,
                    'growth': growth
                },
                'risk_analysis': risk,
                'swot_analysis': swot,
                'recommendations': recommendations,
                'compliance_status': compliance
            }
        except Exception as e:
            raise ValueError(f"Error analyzing company data: {str(e)}")

    def analyze_financials(self, data):
        try:
            revenue = float(data['revenue'])
            profit = float(data['profit'])
            expenses = float(data['expenses'])
            current_assets = float(data['current_assets'])
            current_liabilities = float(data['current_liabilities'])
            inventory = float(data['inventory'])
            
            # Protect against division by zero
            profit_margin = (profit / revenue * 100) if revenue > 0 else 0
            current_ratio = current_assets / current_liabilities if current_liabilities > 0 else 0
            quick_ratio = (current_assets - inventory) / current_liabilities if current_liabilities > 0 else 0
            asset_turnover = revenue / current_assets if current_assets > 0 else 0
            working_capital = current_assets - current_liabilities
            
            # Calculate Z-Score safely
            if current_assets > 0:
                z_score = (1.2 * working_capital / current_assets) + \
                         (1.4 * profit / current_assets) + \
                         (3.3 * (profit + expenses) / current_assets) + \
                         (0.6 * (current_assets / current_liabilities if current_liabilities > 0 else 0)) + \
                         (revenue / current_assets)
            else:
                z_score = 0
            
            return {
                'profit_margin': round(profit_margin, 2),
                'current_ratio': round(current_ratio, 2),
                'quick_ratio': round(quick_ratio, 2),
                'asset_turnover': round(asset_turnover, 2),
                'working_capital': round(working_capital, 2),
                'z_score': round(z_score, 2)
            }
        except Exception as e:
            raise ValueError(f"Error analyzing financial data: {str(e)}")

    def analyze_market_position(self, data):
        try:
            market_share = float(data['market_share'])
            industry = data['industry'].lower()
            total_employees = int(data['total_employees'])
            revenue = float(data['revenue'])
            rd_investment = float(data['rd_investment'])
            
            employee_productivity = revenue / total_employees if total_employees > 0 else 0
            rd_ratio = (rd_investment / revenue * 100) if revenue > 0 else 0
            
            return {
                'market_share': market_share,
                'competitive_position': self._calculate_market_position(market_share),
                'employee_productivity': round(employee_productivity, 2),
                'rd_investment_ratio': round(rd_ratio, 2)
            }
        except Exception as e:
            raise ValueError(f"Error analyzing market position: {str(e)}")

    def analyze_growth(self, data):
        try:
            historical_revenue = [float(x) for x in data['historical_revenue'].split(',')]
            
            if len(historical_revenue) < 2:
                raise ValueError("Insufficient historical revenue data")
            
            growth_rates = []
            for i in range(1, len(historical_revenue)):
                if historical_revenue[i-1] > 0:
                    growth_rate = ((historical_revenue[i] - historical_revenue[i-1]) / historical_revenue[i-1]) * 100
                    growth_rates.append(growth_rate)
            
            avg_growth = np.mean(growth_rates) if growth_rates else 0
            cagr = (((historical_revenue[-1] / historical_revenue[0]) ** (1/len(growth_rates))) - 1) * 100
            
            return {
                'avg_growth_rate': round(avg_growth, 2),
                'cagr': round(cagr, 2),
                'growth_trend': self._determine_growth_trend(growth_rates),
                'historical_data': historical_revenue
            }
        except Exception as e:
            raise ValueError(f"Error analyzing growth data: {str(e)}")

    def analyze_risk(self, data, financial):
        try:
            industry = data['industry'].lower()
            risk_profile = self.risk_profiles.get(industry, {})
            
            financial_risk = self._calculate_financial_risk(financial)
            market_risk = self._calculate_market_risk(data)
            operational_risk = self._calculate_operational_risk(data)
            
            return {
                'financial_risk': round(financial_risk, 2),
                'market_risk': round(market_risk, 2),
                'operational_risk': round(operational_risk, 2),
                'overall_risk': round((financial_risk + market_risk + operational_risk) / 3, 2)
            }
        except Exception as e:
            raise ValueError(f"Error analyzing risk: {str(e)}")

    def generate_swot(self, financial, market, growth):
        """
        Generate an enhanced SWOT analysis with advanced metrics, competitive intelligence,
        and actionable insights.
        """
        strengths = []
        weaknesses = []
        opportunities = []
        threats = []
        
        # Financial Analysis with Industry Benchmarking
        if financial.get('profit_margin', 0) > self.industry_benchmarks.get(industry, {}).get('avg_profit_margin', 20):
            strengths.append({
                'category': 'Financial',
                'subcategory': 'Profitability',
                'description': 'Industry-leading profit margins indicating operational excellence',
                'impact': 'High',
                'metric_value': financial.get('profit_margin'),
                'benchmark_comparison': f"Above industry average by {(financial.get('profit_margin') - self.industry_benchmarks.get(industry, {}).get('avg_profit_margin', 20)):.1f}%",
                'sustainability_score': self._calculate_sustainability_score(financial.get('profit_margin'), historical_margins),
                'recommendation': 'Leverage operational excellence practices across other business units',
                'potential_value': self._calculate_potential_value('profit_optimization'),
                'implementation_complexity': 'Medium',
                'resource_requirements': ['Process documentation', 'Training programs', 'Performance monitoring systems']
            })
        
        # Market Position Analysis with Competitive Intelligence
        market_share = market.get('market_share', 0)
        if market_share > 20:
            strengths.append({
                'category': 'Market',
                'subcategory': 'Market Leadership',
                'description': 'Dominant market position with strong brand recognition',
                'impact': 'High',
                'metric_value': market_share,
                'competitive_analysis': {
                    'market_leader_gap': self._calculate_market_leader_gap(market_share),
                    'brand_strength_index': self._calculate_brand_strength(),
                    'customer_loyalty_score': self._calculate_customer_loyalty(),
                    'market_penetration_rate': self._calculate_market_penetration()
                },
                'recommendation': 'Develop premium market segments and expand service offerings',
                'potential_value': self._calculate_potential_value('market_expansion'),
                'implementation_complexity': 'High',
                'key_success_factors': ['Brand leverage', 'Customer insights', 'Innovation capability']
            })
        
        # Innovation and R&D Analysis
        rd_investment = financial.get('rd_investment', 0)
        rd_ratio = (rd_investment / financial.get('revenue', 1)) * 100
        if rd_ratio < self.industry_benchmarks.get(industry, {}).get('rd_investment_ratio', 10):
            weaknesses.append({
                'category': 'Innovation',
                'subcategory': 'R&D Investment',
                'description': 'Below-industry R&D investment affecting innovation pipeline',
                'impact': 'High',
                'metric_value': rd_ratio,
                'innovation_metrics': {
                    'patent_portfolio_strength': self._analyze_patent_portfolio(),
                    'innovation_success_rate': self._calculate_innovation_success_rate(),
                    'time_to_market': self._calculate_time_to_market(),
                    'rd_efficiency_score': self._calculate_rd_efficiency(rd_investment)
                },
                'recommendation': 'Increase R&D investment and establish innovation hubs',
                'risk_mitigation': ['Structured innovation process', 'Technology partnerships', 'Talent acquisition']
            })
        
        # Digital Transformation Opportunities
        digital_maturity = self._assess_digital_maturity(market)
        if digital_maturity < 0.7:
            opportunities.append({
                'category': 'Digital',
                'subcategory': 'Digital Transformation',
                'description': 'Significant potential for digital optimization and automation',
                'impact': 'High',
                'metric_value': digital_maturity,
                'digital_assessment': {
                    'automation_potential': self._calculate_automation_potential(),
                    'digital_efficiency_gap': self._calculate_digital_efficiency_gap(),
                    'tech_stack_modernity': self._assess_tech_stack(),
                    'digital_talent_readiness': self._assess_digital_talent()
                },
                'recommendation': 'Implement comprehensive digital transformation program',
                'expected_benefits': {
                    'cost_reduction': '15-25%',
                    'productivity_improvement': '20-30%',
                    'customer_experience': 'Significant enhancement',
                    'time_to_market': '40% reduction'
                },
                'implementation_roadmap': ['Infrastructure modernization', 'Process automation', 'Digital upskilling']
            })
        
        # Supply Chain Resilience Analysis
        supply_chain_risk = self._assess_supply_chain_risk()
        if supply_chain_risk > 0.6:
            threats.append({
                'category': 'Operations',
                'subcategory': 'Supply Chain',
                'description': 'High supply chain vulnerability requiring immediate attention',
                'impact': 'High',
                'metric_value': supply_chain_risk,
                'risk_factors': {
                    'supplier_concentration': self._calculate_supplier_concentration(),
                    'geographic_risk': self._assess_geographic_risk(),
                    'inventory_optimization': self._analyze_inventory_optimization(),
                    'logistics_efficiency': self._calculate_logistics_efficiency()
                },
                'recommendation': 'Implement supply chain diversification and resilience program',
                'risk_mitigation_strategies': ['Supplier diversification', 'Inventory optimization', 'Smart logistics'],
                'expected_impact': {
                    'risk_reduction': '40-50%',
                    'cost_optimization': '10-15%',
                    'delivery_reliability': '25% improvement'
                }
            })
        
        # ESG and Sustainability Analysis
        esg_score = self._calculate_esg_score()
        if esg_score < 0.6:
            weaknesses.append({
                'category': 'Sustainability',
                'subcategory': 'ESG Performance',
                'description': 'Below-par ESG performance affecting stakeholder confidence',
                'impact': 'High',
                'metric_value': esg_score,
                'esg_metrics': {
                    'environmental_impact': self._calculate_environmental_impact(),
                    'social_responsibility': self._assess_social_responsibility(),
                    'governance_score': self._calculate_governance_score(),
                    'sustainability_initiatives': self._analyze_sustainability_initiatives()
                },
                'recommendation': 'Develop comprehensive ESG strategy and implementation plan',
                'focus_areas': ['Carbon footprint reduction', 'Social impact programs', 'Governance enhancement'],
                'stakeholder_benefits': ['Improved reputation', 'Risk reduction', 'Access to sustainable finance']
            })
        
        # Talent and Workforce Analysis
        talent_metrics = self._analyze_talent_metrics()
        if talent_metrics['retention_rate'] < 0.85:
            weaknesses.append({
                'category': 'Human Capital',
                'subcategory': 'Talent Management',
                'description': 'High talent attrition affecting organizational capabilities',
                'impact': 'High',
                'metric_value': talent_metrics['retention_rate'],
                'talent_analytics': {
                    'skill_gap_index': self._calculate_skill_gap(),
                    'engagement_score': self._calculate_engagement_score(),
                    'leadership_pipeline': self._assess_leadership_pipeline(),
                    'learning_effectiveness': self._analyze_learning_effectiveness()
                },
                'recommendation': 'Implement comprehensive talent management program',
                'focus_areas': ['Skill development', 'Career progression', 'Employee experience'],
                'expected_outcomes': ['Improved retention', 'Enhanced capabilities', 'Higher productivity']
            })
        
        # Market Expansion Opportunities
        market_potential = self._analyze_market_potential()
        if market_potential['growth_opportunity'] > 0.7:
            opportunities.append({
                'category': 'Growth',
                'subcategory': 'Market Expansion',
                'description': 'Significant untapped market potential in adjacent segments',
                'impact': 'High',
                'metric_value': market_potential['growth_opportunity'],
                'market_analysis': {
                    'addressable_market': self._calculate_addressable_market(),
                    'competition_intensity': self._assess_competition_intensity(),
                    'entry_barriers': self._analyze_entry_barriers(),
                    'success_probability': self._calculate_success_probability()
                },
                'recommendation': 'Develop market expansion strategy with phased implementation',
                'key_initiatives': ['Market research', 'Product adaptation', 'Channel development'],
                'resource_requirements': ['Investment capital', 'Market expertise', 'Local partnerships']
            })
        
        # Calculate priority scores and sort
        impact_scores = {'High': 3, 'Medium': 2, 'Low': 1}
        for category in [strengths, weaknesses, opportunities, threats]:
            for item in category:
                impact_score = impact_scores.get(item['impact'], 1)
                metric_score = min(1, max(0, item.get('metric_value', 0) / 100))
                implementation_complexity = {'Low': 1, 'Medium': 0.7, 'High': 0.4}.get(
                    item.get('implementation_complexity', 'Medium'), 0.7)
                potential_value = item.get('potential_value', 1)
                
                item['priority_score'] = (
                    impact_score * 
                    metric_score * 
                    implementation_complexity * 
                    potential_value
                )
            
            category.sort(key=lambda x: x['priority_score'], reverse=True)
        
        # Generate executive summary with key insights
        summary = {
            'total_factors': len(strengths) + len(weaknesses) + len(opportunities) + len(threats),
            'key_strengths': len([s for s in strengths if s['impact'] == 'High']),
            'key_weaknesses': len([w for w in weaknesses if w['impact'] == 'High']),
            'key_opportunities': len([o for o in opportunities if o['impact'] == 'High']),
            'key_threats': len([t for t in threats if t['impact'] == 'High']),
            'priority_initiatives': self._identify_priority_initiatives(strengths, weaknesses, opportunities, threats),
            'risk_exposure': self._calculate_risk_exposure(threats),
            'growth_potential': self._calculate_growth_potential(opportunities),
            'competitive_position': self._assess_competitive_position(strengths, weaknesses)
        }

        return {
            'strengths': strengths,
            'weaknesses': weaknesses,
            'opportunities': opportunities,
            'threats': threats,
            'summary': summary,
            'timestamp': datetime.now().isoformat(),
            'analysis_version': '2.0'
        }

    def generate_recommendations(self, financial, market, growth, risk, industry):
        """
        Generate strategic recommendations based on company metrics and industry benchmarks.
        
        Parameters:
        -----------
        financial : dict
            Financial metrics including profit_margin
        market : dict
            Market metrics including market_share
        growth : dict
            Growth metrics including growth rate
        risk : dict
            Risk assessment metrics
        industry : str
            Industry classification for benchmark comparison
        
        Returns:
        --------
        list
            List of recommendations with category, priority, description, and actions
        """
        recommendations = []
        benchmark = self.industry_benchmarks.get(industry, {})

        # Financial Performance Recommendations
        if financial['profit_margin'] < benchmark['avg_profit_margin']:
            recommendations.append({
                'category': 'Financial Performance',
                'priority': 'High',
                'description': 'Improve profit margins through cost optimization',
                'actions': [
                    'Review pricing strategy and implement value-based pricing',
                    'Optimize operational costs through process automation',
                    'Evaluate vendor contracts for cost reduction opportunities',
                    'Implement cost tracking and reporting systems',
                    'Develop cost reduction targets by department',
                    'Review resource allocation efficiency'
                ]
            })
        elif financial['profit_margin'] < benchmark['avg_profit_margin'] * 1.1:
            recommendations.append({
                'category': 'Financial Performance',
                'priority': 'Medium',
                'description': 'Maintain and improve current profit margins',
                'actions': [
                    'Monitor cost trends and identify optimization opportunities',
                    'Enhance pricing strategies for premium segments',
                    'Optimize working capital management',
                    'Implement efficiency improvement programs'
                ]
            })

        # Market Position Recommendations
        if market['market_share'] < 15:
            recommendations.append({
                'category': 'Market Position',
                'priority': 'Medium',
                'description': 'Enhance market presence',
                'actions': [
                    'Increase targeted marketing efforts in key segments',
                    'Explore and penetrate new market segments',
                    'Develop clear competitive advantages',
                    'Strengthen brand positioning',
                    'Implement customer retention programs',
                    'Enhance digital presence and capabilities'
                ]
            })
        elif market['market_share'] < 20:
            recommendations.append({
                'category': 'Market Position',
                'priority': 'Medium',
                'description': 'Strengthen market leadership',
                'actions': [
                    'Develop premium market segments',
                    'Enhance customer experience programs',
                    'Expand product/service offerings',
                    'Build strategic partnerships'
                ]
            })

        # Growth Strategy Recommendations
        if growth.get('growth_rate', 0) < benchmark.get('industry_growth', 0):
            recommendations.append({
                'category': 'Growth Strategy',
                'priority': 'High',
                'description': 'Accelerate growth initiatives',
                'actions': [
                    'Develop new product/service lines',
                    'Enter new geographic markets',
                    'Implement innovation program',
                    'Explore strategic acquisitions',
                    'Enhance digital capabilities',
                    'Establish growth metrics and targets'
                ]
            })

        # Risk Management Recommendations
        if risk.get('overall_risk', 0) > benchmark.get('risk_threshold', 0.5):
            recommendations.append({
                'category': 'Risk Management',
                'priority': 'High',
                'description': 'Strengthen risk management framework',
                'actions': [
                    'Implement comprehensive risk assessment',
                    'Develop risk mitigation strategies',
                    'Enhance operational controls',
                    'Establish monitoring systems',
                    'Review insurance coverage',
                    'Develop contingency plans'
                ]
            })

        # Operational Efficiency Recommendations
        if financial.get('operating_margin', 0) < benchmark.get('avg_operating_margin', 0):
            recommendations.append({
                'category': 'Operational Efficiency',
                'priority': 'Medium',
                'description': 'Improve operational efficiency',
                'actions': [
                    'Streamline core business processes',
                    'Implement automation initiatives',
                    'Optimize resource allocation',
                    'Enhance productivity metrics',
                    'Develop performance benchmarks',
                    'Implement continuous improvement program'
                ]
            })

        # Customer Experience Recommendations
        if market.get('customer_satisfaction', 0) < benchmark.get('avg_satisfaction', 85):
            recommendations.append({
                'category': 'Customer Experience',
                'priority': 'Medium',
                'description': 'Enhance customer satisfaction',
                'actions': [
                    'Implement customer feedback system',
                    'Develop service improvement program',
                    'Train customer-facing staff',
                    'Enhance product/service quality',
                    'Improve response times',
                    'Develop customer loyalty programs'
                ]
            })

        # Sort recommendations by priority
        priority_weights = {
            'Critical': 4,
            'High': 3,
            'Medium': 2,
            'Low': 1
        }
        
        # Sort based on priority and number of actions
        recommendations.sort(
            key=lambda x: (
                priority_weights.get(x['priority'], 0),
                len(x['actions'])
            ),
            reverse=True
        )

        # Limit actions to most important ones
        for rec in recommendations:
            rec['actions'] = rec['actions'][:4]  # Keep top 4 most important actions

        return recommendations

    def check_compliance(self, industry, financial):
        compliance_items = [
            {
                'requirement': 'GST Registration',
                'status': 'Required' if financial['working_capital'] > 4000000 else 'Optional',
                'risk_level': 'High',
                'recommendations': 'Ensure timely GST filing and maintain proper documentation'
            },
            {
                'requirement': 'Annual Financial Audit',
                'status': 'Required',
                'risk_level': 'High',
                'recommendations': 'Prepare financial statements and engage certified auditors'
            }
        ]
        
        return compliance_items

    def _calculate_market_position(self, market_share):
        if market_share > 25:
            return 'Market Leader'
        elif market_share > 15:
            return 'Strong Contender'
        elif market_share > 5:
            return 'Established Player'
        return 'Market Follower'

    def _determine_growth_trend(self, growth_rates):
        if not growth_rates:
            return 'Insufficient Data'
        if len(growth_rates) >= 2:
            if growth_rates[-1] > growth_rates[-2]:
                return 'Accelerating'
            elif growth_rates[-1] < growth_rates[-2]:
                return 'Decelerating'
        return 'Stable'

    def _calculate_financial_risk(self, financial):
        risk_score = 1.0
        if financial['current_ratio'] < 1.5:
            risk_score += 0.5
        if financial['quick_ratio'] < 1.0:
            risk_score += 0.5
        if financial['profit_margin'] < 10:
            risk_score += 0.5
        if financial['z_score'] < 1.8:
            risk_score += 0.5
        return min(risk_score, 3.0)

    def _calculate_market_risk(self, data):
        market_share = float(data['market_share'])
        competitors = int(data['competitors'])
        
        risk_score = 1.0
        if market_share < 10:
            risk_score += 0.5
        if competitors > 10:
            risk_score += 0.5
        return min(risk_score, 3.0)

    def _calculate_operational_risk(self, data):
        employee_count = int(data['total_employees'])
        revenue = float(data['revenue'])
        
        risk_score = 1.0
        if employee_count < 50:
            risk_score += 0.5
        if revenue < 10000000:  # 1 crore
            risk_score += 0.5
        return min(risk_score, 3.0)

@app.route('/analyze', methods=['POST'])
def analyze():
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No data provided'}), 400
        
        analyzer = BusinessAnalyzer()
        result = analyzer.analyze_company(data)
        return jsonify(result)
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': f'Internal server error: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True)
