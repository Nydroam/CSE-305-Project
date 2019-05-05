import React, { Component } from 'react';
import MenuBar from './MenuBar';
import axios from 'axios';
import  { Item, Button, Label, Image}  from 'semantic-ui-react';

class Listing extends Component {
    
    state = {}

    async storeData(){
        await axios.get('http://localhost:5000/listing')
        .then((response) => {
            this.setState({data: response.data});
            response.data.map((item)=>{
                this.setState({[item[0]]: 0});
            })
        })
        .catch((error)=> {
            console.log(error);
        });
    }

    addtoCart(){
        this.props.history.push({
            pathname: '/cart',
            state: this.state
          });
    }

    buildCard(){
        return this.state.data.map((item) => {
            let name = item[0];
            let amount = this.state[name];
            return(
                <Item key={item[0]}>
                    <Item.Image size = 'tiny' src= {require(`../sample_images/${item[0]}.PNG`)} />
                    <Item.Content>
                        <Item.Header>{item[2]}</Item.Header>
                        <Item.Description>{`Item price: $${item[3]}`}</Item.Description>
                        <Item.Description>{`Item Stock: ${item[5]}`}</Item.Description>
                        <Item.Description>{`Item Seller: ${item[4]}`}</Item.Description>
                        <Item.Extra>
                            <Label>{`${item[1]}`}</Label>
                            <Button floated='right' onClick={()=> this.setState({[item[0]]:amount+=1})} disabled={amount === item[5] ? true: false}>+</Button>
                            <Button floated='right'>{amount}</Button>
                            <Button floated='right' onClick={()=>this.setState({[item[0]]:amount-=1})} disabled={amount === 0 ? true : false}>-</Button> 
                            <Button floated='right' disabled={true}>{`Total: $${amount*item[3]}`}</Button>
                        </Item.Extra>
                    </Item.Content>
                </Item>
            );
        });
    }

    componentDidMount(){
        this.storeData();
    }

    render(){
        const {data}  = this.state;
        if(data){
            return(
                <div>
                    <MenuBar active='listing' />
                    <Item.Group divided>
                        {this.buildCard()}
                        <Item>
                            <Item.Extra>
                                <Button primary size = "huge" floated='right' onClick={()=>this.addtoCart()}>Add to Cart</Button>
                            </Item.Extra>
                        </Item>
                    </Item.Group>
                </div>
            );
        }
        else{
            return(
                <div>
                    <MenuBar />
                </div>
            );
        }
        
    }

}

export default Listing;