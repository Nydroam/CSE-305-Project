import React from 'react';
import  { Menu }  from 'semantic-ui-react';
import { Link } from 'react-router-dom';

const MenuBar = (e) => {
    return(
        <div>
            <Menu widths = '4' inverted>
                <Menu.Item>
                    <Link to='/'> Home </Link>
                </Menu.Item>
                <Menu.Item>
                    <Link to='/listing'>Listing</Link>
                </Menu.Item>
                <Menu.Item>
                    <Link to='/Cart'> Cart </Link>
                </Menu.Item>
            </Menu>
        </div>
    )
}

export default MenuBar;