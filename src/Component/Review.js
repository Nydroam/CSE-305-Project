import React, { Component } from 'react';
import MenuBar from './MenuBar';
import axios from 'axios';
import  { Item, Dimmer, Rating, Loader, Label } from 'semantic-ui-react';
class Review extends Component{
	state = {}

    componentDidMount(){
    	const{match:{params	}} = this.props;

    	axios.get(`http://localhost:5000/review/${params.id}`)
    	.then((response) => {
    		this.setState({data: response.data});
    	})
    	.catch((error)=> {
            console.log(error);
        });
    }

    buildCard(){
        return this.state.data[1].map((item) => {
            return(
                <Item>
                <Item.Content>
                <Rating icon='star' disabled defaultRating={item[0]} maxRating={5} />
              
                <Item.Description>"{item[1]}"</Item.Description>
                </Item.Content>
                    
                </Item>
            );
        });
    }

    render(){
    	const{data} = this.state;
    	const{match:{params	}} = this.props;
    	if(data){
            return(
                <div>
                    <MenuBar active='listing' />
                    <Item.Group divided>
                    <Item>
                   		<Item.Image size='small' src={require(`../sample_images/${params.id}.PNG`)} />
                    	<Item.Content verticalAlign='top'>
                    	<Item.Header>{data[0][0]} </Item.Header>
                    	<Item.Description>{`Price: $${data[0][1]}`}</Item.Description>
                    	<Item.Description>{`Seller: ${data[0][2]}`}</Item.Description>
                    	<Item.Extra>
                    	<Rating icon='star' disabled defaultRating={data[0][4]} maxRating={5} />
                    	<Label>{`${data[0][3]}`}</Label>
                    	</Item.Extra>
                    	</Item.Content>
                    </Item>
                        {this.buildCard()}
                    </Item.Group>
                </div>
            );
        }
        else{
            return(
                <div>
                    <MenuBar />
                    <Dimmer active>
                        <Loader />
                    </Dimmer>
                </div>
            );
        }
    }

}

export default Review;