import pandas as pd
import pymc as pm
import arviz as az


path='./'
XRB_model_sample_sample_prior_predictive = az.from_netcdf(path+'fake_XRB_model_sample_prior_predictive.nc')
XRB_model_mcmc_sample = az.from_netcdf(path+'fake_XRB_model_mcmc_sample.nc')
DATA = pd.read_csv(path+'fake_data.csv')

print('Contingency data loaded. Please follow these instructions and use these for questions 5 and later:')
print('- Fake data is accessible as "contingency.DATA".\n\tUse this data instead of original data.')
print('- Inference data containing posterior and posterior_predictive samples is accessible as "contingency.XRB_model_mcmc_sample".\n\tUse this to replace your XRB_model_mcmc_sample.')
print('- Inference data containing only prior samples is accessible as "contingency.XRB_model_sample_sample_prior_predictive".\n\tUse this to replace your XRB_model_sample_prior_predictive inference data.')
