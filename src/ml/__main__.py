"""Command-line demo: ``python -m ml [numbers...]``."""

from __future__ import annotations

from sklearn.neighbors import KNeighborsRegressor
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neighbors import KNeighborsTransformer
from sklearn.tree import DecisionTreeRegressor


if __name__ == "__main__":
    x_train = [[5,2,3],[5,6,2],[1,9,7],[3,4,8],[2,9,6]]
    y_train = [5,1,2,3,4]
    x_test = [[3,2,7]]
    estimator_re = KNeighborsRegressor(n_neighbors=4)
    estimator_re.fit(x_train, y_train)
    y_pred_re = estimator_re.predict(x_test)

    print(y_pred_re)

    estimator_cl = KNeighborsClassifier(n_neighbors=2)
    estimator_cl.fit(x_train, y_train)
    y_pred_cl = estimator_cl.predict(x_test)

    print(y_pred_cl)


