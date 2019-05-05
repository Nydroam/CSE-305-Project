import React, {Component} from 'react';
import  { Menu }  from 'semantic-ui-react';
import { Link } from 'react-router-dom';

class MenuBar extends Component{
    render(){
        return(
            <div>
                <Menu widths = '4'>
                    <Menu.Item active={this.props.active === 'home' ? true : false}>
                        <Link to='/'> Home </Link>
                    </Menu.Item>
                    <Menu.Item active={this.props.active === 'listing' ? true : false}>
                        <Link to='/listing'>Listing</Link>
                    </Menu.Item>
                    <Menu.Item active={this.props.active === 'cart' ? true : false}>
                        <Link to='/cart'> Cart </Link>
                    </Menu.Item>
                </Menu>
            </div>
        )
    }
}

export default MenuBar;