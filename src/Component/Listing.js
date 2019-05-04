import React, { Component } from 'react';
import MenuBar from './MenuBar'
import axios from 'axios'

class Listing extends Component {

    componentWillMount(){
        axios.get('/user?ID=12345')
        .then(function (response) {
            console.log(response);
        })
        .catch(function (error) {
            console.log(error);
        });
    }

    render(){
        return(
            <div>
                <MenuBar />
                Listing
            </div>
        );
    }

}

export default Listing;