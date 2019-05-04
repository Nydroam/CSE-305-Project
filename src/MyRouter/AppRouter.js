import React from 'react';
import { Router, Route, Switch } from 'react-router-dom';
import Listing from '../Component/Listing';
import Index from '../Component/Index';
import Cart from '../Component/Cart';
import { createBrowserHistory } from 'history'

export const history = createBrowserHistory();

const AppRouter = () => (
    <Router history={history}>
        <div>
        <Switch>
            <Route exact path="/" component={Index} />
            <Route path="/cart" component={Cart} />
            <Route path="/listing" component={Listing} />
        </Switch>
        </div>
    </Router>
);

export default AppRouter;