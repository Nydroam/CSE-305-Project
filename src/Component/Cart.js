import React, { Component } from 'react';
import MenuBar from './MenuBar'
import axios from 'axios';
import { Segment, Image, Button} from 'semantic-ui-react'

class Cart extends Component {
    
    state = {}

    async getData(){
        await axios.get('http://localhost:5000/cart').then((data) =>{
            this.setState({data:data.data});
        }).catch((error)=> {
            console.log(error);
        });
    }

    purchase(){
        axios.get('http://localhost:5000/purchase');
        this.props.history.push({
            pathname: '/success',
        });
    }

    componentDidMount(){
        this.getData();
    }

    sumAll(){
        let arr = this.state.data.map((item) => item[0]);
        let total = arr.reduce((a,b)=>a+b)
        return total.toFixed(2);
    }

    buildSegment(){
        return this.state.data.map((item)=>{
            return(
                <Segment key={item[1]}>
                    <Image size = 'tiny' src= {require(`../sample_images/${item[1]}.PNG`)} />
                    {`Name: ${item[3]}`}<br />
                    {`Price per item: $${item[4]}`}<br />
                    {`Amount added: ${item[2]}`}<br />
                    {`Total price: $${item[0]}`}
                </Segment>
            );
        })
    }

    render(){
        const {data} = this.state;
        console.log(data);
        if(data && data.length){
            return(
                <div>
                    <MenuBar active='cart'/>
                    <Segment.Group>
                        {this.buildSegment()}
                    </Segment.Group>
                    <Button>{`Total overall: $${this.sumAll()}`}</Button>
                    <Button onClick={()=> this.purchase()} positive>Purchase</Button>
                </div>
            );
        }
        else{
            return(
                <div>
                    <MenuBar />
                    No Items in Cart
                </div>
            );
        }
    }

}

export default Cart;