import React, { Component } from 'react';
import MenuBar from './MenuBar'
import axios from 'axios';

class Cart extends Component {

    componentDidMount(){
        let arr = this.props.location.state;
        delete arr['data'];
        axios.post('http://localhost:5000/addcart',
           {...arr}
        );
    }

    render(){
        console.log(this.props);
        return(
            <div>
                <MenuBar active='cart'/>
                Cart
            </div>
        );
    }

}

export default Cart;