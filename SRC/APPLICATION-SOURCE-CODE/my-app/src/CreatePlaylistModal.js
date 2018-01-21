import React, { Component, ReactSlider } from "react";
import {Modal, Button, ButtonGroup, FormGroup, InputGroup, FormControl } from "react-bootstrap";
import Slider from 'react-rangeslider';
import 'react-rangeslider/lib/index.css';


import "./CreatePlaylistModal.css";

export default class CreatePlaylistModal extends Component {
    constructor (props, context) {
        super(props, context)
        this.state = {
          name: '',
          danceabilityValue: 10,
          energyValue: 10,
          freeSearchType: '',
          freeSearchData: '',
          tags: ''
        }
    }
    
    validateForm() {
        return this.state.name.length > 0;
    }
    
    nameHandleChange(value) {
        this.setState({name: value})
    }
    
    danceabilityHandleChange(value) {
        this.setState({
          danceabilityValue: value
        })
    }

    energyHandleChange(value) {
        this.setState({
          energyValue: value
        })
    }

    tagsHandleChange(value) {
        this.setState({tags: value})
    }
    
    
    render() {
        return (
            <div>  
                <Modal show={this.props.show} hide={this.props.onHide}>
                    <button type="button" className="close" onClick={this.props.onHide}>
                        <span>&times;</span>
                    </button>
                
                    <h2 class="modal-title">find new playlist</h2>
                    <h4 class="playlist name">choose a name for your playlist</h4>
                    <FormGroup>
                        <InputGroup>
                            <FormControl type="text" onChange={(e) => this.nameHandleChange(e.target.value)} value={this.state.name} />
                        </InputGroup>
                    </FormGroup>
                        
                    <h4 class="danceability">choose danceability value for your playlist</h4>
                    <div className='slider'>
                        <Slider 
                            min={0}
                            max={1000}
                            value={this.state.danceabilityValue}
                            onChange={(value) => this.danceabilityHandleChange(value)}
                        />
                        <div className='value'>{this.state.danceabilityValue}</div>
                    </div>
                    
                    <h4 class="energy">choose energy value for your playlist</h4>
                    <div className='slider'>
                        <Slider 
                            min={0}
                            max={1000}
                            value={this.state.energyValue}
                            onChange={(value) => this.energyHandleChange(value)}
                        />
                        <div className='value'>{this.state.energyValue}</div>
                    </div>
                    
                    
                    <div className="Tags">
                        <h4>what tag you want to search:</h4>
                        <FormGroup>
                            <InputGroup>
                                <FormControl type="text" onChange={(e) => this.tagsHandleChange(e.target.value)} value={this.state.tags} />
                            </InputGroup>
                        </FormGroup>
                    </div>
                    
                    <br/>
                    <Button bsStyle="primary" disabled={!this.validateForm()} onClick={() => {this.props.findNewPlaylist(this.state)}}>find playlist</Button>
                </Modal>
            </div>
        );
    }    
}
