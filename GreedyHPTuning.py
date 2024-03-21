from sklearn.model_selection import GridSearchCV
import matplotlib.pyplot as plt
def hppmtuner(XTrain,YTrain,model,param_grid,bp,cv):
  grid_search = GridSearchCV(model,param_grid,n_jobs=-1,verbose=2,
                            cv=cv,scoring='neg_mean_absolute_percentage_error')
  grid_search.fit(XTrain, YTrain)
  param_grid.popitem()
  v = grid_search.best_params_[bp]
  param_grid[bp] = [v]
  return param_grid, grid_search
def GreedyGSCV(XTrain,YTrain,model,param_grid,cv=3):
  pg = {}
  for i in range(len(param_grid)):
    k,v = list(param_grid.items())[i]
    pg.update({k:v})
    print("Tuning Hyperparameter :",k)
    pg, gs = hppmtuner(XTrain,YTrain,model,pg,k,cv)
    mts = -gs.cv_results_['mean_test_score']*100
    f, ax = plt.subplots()
    plt.plot(range(len(v)),mts)
    plt.xticks(range(len(v)),[str(i) if i is not None else 'None' for i in v])
    plt.xlabel(k)
    plt.ylabel("MAPE (%)")
    plt.title(f"Variation of Error while tuning {k}")
    er = min(mts)
    mne = f"Min Error = {er:.3f}% at {k} = {v[list(mts).index(er)]}"
    plt.text(0.1,0.9,mne,transform=ax.transAxes)
    plt.grid()
    plt.show()
    print("\nOptimal Feature Set :",pg)
    print("Best Estimator :",gs.best_estimator_,'\n')
