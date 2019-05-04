import React, { Component } from 'react';
import MenuBar from './MenuBar'
import  { Header, Icon }  from 'semantic-ui-react';

class Index extends Component {
    render(){
        return(
            <div>
                <MenuBar />
                <div style={{position: 'relative', top:'100px'}}>
                    <Header as='h1' icon textAlign='center'>
                        <Icon name='shopping bag' circular />
                        <Header.Content>Shop</Header.Content>
                    </Header>
                </div>
            </div>
        );
    }

}

export default Index;
