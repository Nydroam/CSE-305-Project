import React from 'react';
import { Router, Route, Switch } from 'react-router-dom';
import Listing from '../Component/Listing';
import Index from '../Component/Index';
import Cart from '../Component/Cart';
import Success from '../Component/Success';
import Review from '../Component/Review';
import { createBrowserHistory } from 'history'

export const history = createBrowserHistory();

const AppRouter = () => (
    <Router history={history}>
        <div>
        <Switch>
            <Route exact path="/" component={Index} />
            <Route exact path="/review/:id" component={Review} />
            <Route path="/cart" component={Cart} />
            <Route path="/listing" component={Listing} />
            <Route path="/success" component={Success} />
        </Switch>
        </div>
    </Router>
);

export default AppRouter;