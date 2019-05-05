import React, { Component } from 'react';
import MenuBar from './MenuBar'
import axios from 'axios';

class Cart extends Component {

    componentDidMount(){
        axios.post('http://localhost:5000/addcart',
           {...this.props.location.state}
        );
    }

    filtering(){
        this.props.location.state.map((item)=>{
            if(item !== 'data'){
                return(
                    <div>
                    </div>
                );
            }
            return null;
        })
    }

    render(){
        console.log(this.props);
        return(
            <div>
                <MenuBar active='cart'/>
            </div>
        );
    }

}

export default Cart;