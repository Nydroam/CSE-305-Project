import React, { Component } from 'react';
import MenuBar from './MenuBar'
import  { Header, Icon }  from 'semantic-ui-react';

class Success extends Component {
    render(){
        return(
            <div>
                <MenuBar/>
                <div style={{position: 'relative', top:'100px'}}>
                    <Header as='h1' icon textAlign='center'>
                        Sucessfully purchased
                    </Header>
                </div>
            </div>
        );
    }

}

export default Success;
