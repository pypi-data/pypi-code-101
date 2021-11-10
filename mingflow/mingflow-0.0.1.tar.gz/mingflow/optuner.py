import optuna


class Optuner:
    def __init__(self):
        pass
    def run_optuna(self, objective, n_trials=20):
        n_trials=n_trials
        print('Started..')
        study = optuna.create_study(direction='maximize')
        print(study)
        study.optimize(objective, n_trials=n_trials) # 100个trails
        print('Number of finished trials:', len(study.trials))
        print('Best trial:', study.best_trial.params)
        return study

    def get_objective(self, X, y, model_wrapper, get_params_func, direction, **kwargs):
        def objective(
            trial, 
            data=X, 
            target=y, 
            model_wrapper=model_wrapper, 
            direction=direction,
            **kwargs
        ):
            params = get_params_func(trial)
            best_score = model_wrapper.cv(X, y, params, get_best=True, direction=direction)
            return best_score

        return objective
    
